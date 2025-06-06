# Generated by Django 5.2 on 2025-05-22 12:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0016_news_description_de_news_description_en_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="answeroption",
            name="text_de",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="answeroption",
            name="text_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="blockinfo",
            name="description_de",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="blockinfo",
            name="description_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="blockinfo",
            name="title_de",
            field=models.CharField(max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="blockinfo",
            name="title_en",
            field=models.CharField(max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="title_de",
            field=models.CharField(max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="title_en",
            field=models.CharField(max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="dateprice",
            name="title_de",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="dateprice",
            name="title_en",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="accomodation_de",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="accomodation_en",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="description_de",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="description_en",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="map_de",
            field=models.FileField(blank=True, null=True, upload_to="maps/"),
        ),
        migrations.AddField(
            model_name="destination",
            name="map_en",
            field=models.FileField(blank=True, null=True, upload_to="maps/"),
        ),
        migrations.AddField(
            model_name="destination",
            name="mini_title_de",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="mini_title_en",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="title_de",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="title_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="transportation_de",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="transportation_en",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="type_de",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="destination",
            name="type_en",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_de",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_en",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_de",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="features",
            name="title_de",
            field=models.CharField(max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="features",
            name="title_en",
            field=models.CharField(max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="itenary",
            name="title_de",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="itenary",
            name="title_en",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="text_de",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="text_en",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="quiz",
            name="description_de",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="quiz",
            name="description_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="quiz",
            name="title_de",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="quiz",
            name="title_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="review",
            name="content_de",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="review",
            name="content_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="review",
            name="country_de",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="review",
            name="country_en",
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="tag",
            name="title_de",
            field=models.CharField(max_length=123, null=True),
        ),
        migrations.AddField(
            model_name="tag",
            name="title_en",
            field=models.CharField(max_length=123, null=True),
        ),
    ]
