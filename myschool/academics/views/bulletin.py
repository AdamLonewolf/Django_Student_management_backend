# accounts/views/bulletin.py
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from academics.models.mark import Mark
from accounts.models.student import Student

class BulletinView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        # Récupère l'étudiant
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return HttpResponse("Étudiant introuvable", status=404)

        # Récupère ses notes
        marks = Mark.objects.filter(enrollment__student=student)

        # Génère le PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="bulletin_{student.student_number}.pdf"'

        doc = SimpleDocTemplate(response, pagesize=A4)
        styles = getSampleStyleSheet()
        elements = []

        # Titre
        elements.append(Paragraph("EduManage - Bulletin de notes", styles['Title']))
        elements.append(Spacer(1, 20))

        # Infos étudiant
        elements.append(Paragraph(f"Étudiant : {student.user.first_name} {student.user.last_name}", styles['Normal']))
        elements.append(Paragraph(f"N° Étudiant : {student.student_number or '—'}", styles['Normal']))
        elements.append(Paragraph(f"Niveau : {student.level.name if student.level else '—'}", styles['Normal']))
        elements.append(Spacer(1, 20))

        # Tableau des notes
        data = [['Cours', 'Note /20', 'Appréciation', 'Date']]
        total = 0
        for mark in marks:
            data.append([
                mark.enrollment.course.name,
                str(mark.mark),
                mark.remark or '—',
                mark.graded_at.strftime('%d/%m/%Y') if mark.graded_at else '—'
            ])
            total += float(mark.mark)

        # Moyenne
        if marks:
            moyenne = total / marks.count()
            data.append(['', f'Moyenne : {moyenne:.2f}/20', '', ''])

        table = Table(data, colWidths=[200, 80, 120, 80])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c2c2c')), 
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black), 
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black), 
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
            ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#e0e0e0')),
            ('TEXTCOLOR', (0, -1), (-1, -1), colors.black),  
        ]))
        elements.append(table)

        doc.build(elements)
        return response