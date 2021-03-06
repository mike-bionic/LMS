from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Length,ValidationError


class UniversityForm(FlaskForm):
	university_name = StringField('Uniwersitetiň ady:',validators=[DataRequired()])
	university_description = StringField('Beýany:')
	logo = FileField('Logo:',validators=[FileAllowed(['png','img','jpg','jpeg'])])
	submit = SubmitField('Üýtget')


class UploadFileForm(FlaskForm):
	file = FileField('Faýl ýükläň')
	submit = SubmitField('Ýükle')


class PostLessonForm(FlaskForm):
	lesson_name = StringField('Temanyň ady:',validators=[DataRequired()])
	lesson_description = StringField('Beýany:')
	subject = SelectField('Dersiň ady:',coerce=int,validators=[DataRequired()])
	major = SelectField('Ugry:',coerce=int,validators=[DataRequired()])
	attachment = FileField('Sapak ýükläň:',validators=[FileAllowed(
		['mp4','mov','3gp','webm','jpg','jpeg','doc','docx','txt','odt','pdf','djvu'])])
	submit = SubmitField('Ýükle')


class AddAttachmentForm(FlaskForm):
	filename = StringField('Faýlyň ady:',validators=[DataRequired()])
	attachment = FileField('Faýl:',validators=[FileAllowed(
		['mp4','mov','3gp','webm','jpg','jpeg','doc','docx','txt','odt','pdf','djvu'])])
	submit = SubmitField('Ýükle')


class PostReferenceForm(FlaskForm):
	reference_name = StringField('Kitabyň ady:',validators=[DataRequired()])
	reference_description = StringField('Beýany:')
	major = SelectField('Ugruň ady:',coerce=int,validators=[DataRequired()])
	attachment = FileField('Sapak ýükläň:',validators=[FileAllowed(
		['mp4','mov','3gp','webm','jpg','jpeg','doc','docx','txt','odt','pdf','djvu'])])
	submit = SubmitField('Ýükle')


class PostHometaskForm(FlaskForm):
	hometask_name = StringField('Ýumuşyň ady:',validators=[DataRequired()])
	hometask_description = StringField('Beýany:')
	subject = SelectField('Dersiň ady:',coerce=int,validators=[DataRequired()])
	major = SelectField('Ugry:',coerce=int,validators=[DataRequired()])
	attachment = FileField('Faýl ýükläň:')
	submit = SubmitField('Ýükle')


class PostSolutionForm(FlaskForm):
	solution_name = StringField('Çözgüdiň ady:',validators=[DataRequired()])
	solution_description = StringField('Beýany:')
	completed = BooleanField()
	attachment = FileField('Faýl ýükläň:')
	submit = SubmitField('Ýükle')