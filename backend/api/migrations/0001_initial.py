# Generated by Django 5.1.2 on 2024-10-31 15:01

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendeeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('phone_number', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, default='Attendee', max_length=50, null=True)),
                ('address', models.CharField(blank=True, default=' ', max_length=500, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=9, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('company', models.CharField(blank=True, max_length=200)),
                ('facebook_profile', models.URLField(blank=True)),
                ('instagram_handle', models.CharField(blank=True, max_length=50)),
                ('nationality', models.CharField(default='', max_length=100)),
                ('attended_events_count', models.PositiveIntegerField(default=0)),
                ('cancelled_events_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('groups', models.ManyToManyField(blank=True, related_name='attendeeuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='attendeeuser_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('organization_type', models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('COMPANY', 'Company'), ('NONPROFIT', 'Non-Profit Organization'), ('EDUCATIONAL', 'Educational Institution'), ('GOVERNMENT', 'Government Organization')], default='INDIVIDUAL', max_length=20)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='organizer_logos/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('description', models.TextField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_handle', models.CharField(blank=True, max_length=50)),
                ('instagram_handle', models.CharField(blank=True, max_length=50)),
                ('youtube_channel', models.URLField(blank=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('verification_status', models.CharField(choices=[('PENDING', 'Pending'), ('VERIFIED', 'Verified'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Event Created At')),
                ('start_date_event', models.DateTimeField(verbose_name='Event Start Date')),
                ('end_date_event', models.DateTimeField(blank=True, verbose_name='Event End Date')),
                ('start_date_register', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration Start Date')),
                ('end_date_register', models.DateTimeField(verbose_name='Registration End Date')),
                ('description', models.TextField(max_length=400)),
                ('max_attendee', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('address', models.CharField(blank=True, default=' ', max_length=500, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=9, null=True)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='event_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])])),
                ('is_free', models.BooleanField(default=True)),
                ('ticket_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('expected_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_online', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('CONFERENCE', 'Conference'), ('WORKSHOP', 'Workshop'), ('SEMINAR', 'Seminar'), ('NETWORKING', 'Networking'), ('CONCERT', 'Concert'), ('SPORTS', 'Sports'), ('OTHER', 'Other')], default='OTHER', max_length=50)),
                ('tags', models.CharField(blank=True, help_text='Comma-separated tags', max_length=200)),
                ('detailed_description', models.TextField(blank=True, help_text='Full event details including schedule')),
                ('status', models.CharField(default='', max_length=20)),
                ('dress_code', models.CharField(choices=[('CASUAL', 'Casual'), ('SMART_CASUAL', 'Smart Casual'), ('BUSINESS_CASUAL', 'Business Casual'), ('SEMI_FORMAL', 'Semi-Formal'), ('FORMAL', 'Formal'), ('BLACK_TIE', 'Black Tie'), ('WHITE_TIE', 'White Tie'), ('THEMED', 'Themed Dress Code'), ('OUTDOOR_BEACH_CASUAL', 'Outdoor/Beach Casual')], max_length=20)),
                ('status_registeration', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed'), ('FULL', 'Full'), ('PENDING', 'Pending'), ('CANCELLED', 'Cancelled'), ('WAITLIST', 'Waitlist')], max_length=20)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('contact_phone', models.CharField(blank=True, max_length=20)),
                ('website_url', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('min_age_requirement', models.PositiveIntegerField(default=0, help_text='Minimum age required to attend the event', validators=[django.core.validators.MaxValueValidator(100)])),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('terms_and_conditions', models.TextField(blank=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api.organizer')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=255)),
                ('session_type', models.CharField(choices=[('POLLS', 'Polls'), ('COMMENT', 'Comment'), ('FEEDBACK', 'Feedback')], default='POLLS', max_length=20)),
                ('description', models.TextField(blank=True)),
                ('max_attendee', models.PositiveIntegerField(default=0)),
                ('event_create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Session Created At')),
                ('start_date_event', models.DateTimeField(verbose_name='Session Start Date')),
                ('end_date_event', models.DateTimeField(verbose_name='Session End Date')),
                ('start_date_register', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration Start Date')),
                ('end_date_register', models.DateTimeField(verbose_name='Registration End Date')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='api.event')),
            ],
            options={
                'ordering': ['start_date_event'],
                'indexes': [models.Index(fields=['event', 'start_date_event'], name='api_session_event_i_810950_idx'), models.Index(fields=['session_type'], name='api_session_session_21db26_idx')],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date registered')),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('CANCELLED', 'Cancelled'), ('EXPIRED', 'Expired')], default='ACTIVE', max_length=20)),
                ('ticket_number', models.CharField(default='', editable=False, max_length=100, unique=True)),
                ('cancellation_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
            ],
            options={
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['ticket_number'], name='api_ticket_ticket__f596c7_idx'), models.Index(fields=['status'], name='api_ticket_status_874e9d_idx'), models.Index(fields=['register_date'], name='api_ticket_registe_9c3cbd_idx')],
                'constraints': [models.UniqueConstraint(fields=('event', 'attendee'), name='unique_event_attendee')],
            },
        ),
    ]
