# Generated by Django 5.2 on 2025-05-27 13:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0019_faqcategory_faq_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faqcategory",
            name="description",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="faqcategory",
            name="description_de",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="faqcategory",
            name="description_en",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
