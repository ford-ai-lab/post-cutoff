# django (pypi): changes after 2025-06-01

- Latest stable on the registry: **6.1.3** (2026-11-03). Built 2026-11-25.
- 48 stable releases after the cut-off: 4.2.22 (2025-06-04) to 6.1.3 (2026-11-03).
- New major versions since the cut-off: 6.0 (2025-12-03).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 6.1 (2026-08-05) [source](https://github.com/django/django/blob/main/docs/releases/6.1.txt)
- Database backend API: This section describes changes that may be needed in third-party database backends.
- The `DatabaseOperations.adapt_durationfield_value()` hook is added. If the database has native support for `DurationField`, override this method to simply return the value.
- The `DatabaseIntrospection.get_relations()` should now return a dictionary with 3-tuples containing (`field_name_other_table`, `other_table`, `db_on_delete`) as values. […]
- Set the new `DatabaseFeatures.supports_inspectdb` attribute to `False` if the management command isn't supported.
- The `DatabaseFeatures.prohibits_dollar_signs_in_column_aliases` feature flag is removed.
- The `DatabaseOperations.binary_placeholder_sql()` method now expects a query compiler as an extra positional argument and should return a two-elements tuple composed of an SQL format string and a tuple of associated parameters.
- The `BaseSpatialOperations.get_geom_placeholder()` method is renamed to `get_geom_placeholder_sql` and is expected to return a two-elements tuple composed of an SQL format string and a tuple of associated parameters.
- Set the new `DatabaseFeatures.supports_bit_aggregations` attribute to `False` if the database doesn't support bitwise aggregations.
- The `wide` class is removed, as it was made obsolete by the new layout.
- The `object-tools` block is hoisted out of the `content` block in forms.
- The undocumented `InclusionAdminNode.init()` now takes the template tag `name` as the first positional argument.
- The undocumented `ChangeList.has_related_field_in_list_display()` method has been replaced with `ChangeList.get_select_related_fields()`.
### 6.0 (2025-12-03) [source](https://github.com/django/django/blob/main/docs/releases/6.0.txt)
- Database backend API: This section describes changes that may be needed in third-party database backends.
- `django.db.backends.base.schema.BaseDatabaseSchemaEditor` and PostgreSQL backends no longer use `CASCADE` when dropping a column.
- `DatabaseOperations.return_insert_columns()` and `DatabaseOperations.fetch_returned_insert_rows()` methods are renamed to `returning_columns()` and `fetch_returned_rows()`, respectively, to denote they can be used in the context […]
- The `DatabaseOperations.fetch_returned_insert_columns()` method is removed and the `fetch_returned_rows()` method replacing `fetch_returned_insert_rows()` expects both a `cursor` and `returning_params` to be provided, just like […]
- If the database supports `UPDATE … RETURNING` statements, backends can set `DatabaseFeatures.can_return_rows_from_update=True`.
- Dropped support for MariaDB 10.5: Upstream support for MariaDB 10.5 ends in June 2025. Django 6.0 supports MariaDB 10.6 and higher.
- `aiosmtpd` 1.4.5
- `argon2-cffi` 23.1.0
- `bcrypt` 4.1.1
- `docutils` 0.22
- `geoip2` 4.8.0
- `Pillow` 10.1.0
- (35 more in this category not shown; see the changelog.)

## Removed or renamed
### 6.1 (2026-08-05) [source](https://github.com/django/django/blob/main/docs/releases/6.1.txt)
- `Permission.name` and `Permission.codename` values are now renamed when renaming models via a migration.
- These features have reached the end of their deprecation cycle and are removed in Django 6.1.
- See `deprecated-features-5.2` for details on these changes, including how to remove usage of these features.
- The `all` parameter for the `django.contrib.staticfiles.finders.find()` function is removed in favor of the `find_all` parameter.
- Fallbacks to `request.user` and `request.auser()` when `user` is `None` in `django.contrib.auth.login()` and `django.contrib.auth.alogin()`, respectively, are removed.
- The `ordering` keyword parameter of the PostgreSQL specific aggregation functions `django.contrib.postgres.aggregates.ArrayAgg`, `django.contrib.postgres.aggregates.JSONBAgg`, and `django.contrib.postgres.aggregates.StringAgg` […]
- Support for subclasses of `RemoteUserMiddleware` that override `process_request()` without overriding `aprocess_request()` is removed.
### 6.0 (2025-12-03) [source](https://github.com/django/django/blob/main/docs/releases/6.0.txt)
- These features have reached the end of their deprecation cycle and are removed in Django 6.0.
- See `deprecated-features-5.0` for details on these changes, including how to remove usage of these features.
- Support for passing positional arguments to `BaseConstraint` is removed.
- The `DjangoDivFormRenderer` and `Jinja2DivFormRenderer` transitional form renderers are removed.
- `BaseDatabaseOperations.field_cast_sql()` is removed.
- `request` is required in the signature of `ModelAdmin.lookup_allowed()` subclasses.
- Support for calling `format_html()` without passing args or kwargs is removed.
- (20 more in this category not shown; see the changelog.)

## Deprecated
### 6.1 (2026-08-05) [source](https://github.com/django/django/blob/main/docs/releases/6.1.txt)
- Until then, the older settings will continue to work but will issue deprecation warnings: see the list of `email deprecations` below.
- The `EMAIL_BACKEND`, `EMAIL_FILE_PATH`, `EMAIL_HOST`, `EMAIL_HOST_PASSWORD`, `EMAIL_HOST_USER`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_USE_SSL`, `EMAIL_SSL_CERTFILE`, `EMAIL_SSL_KEYFILE`, and `EMAIL_TIMEOUT` settings are […]
- `mail.get_connection` is deprecated. See `migrating-to-mailers-get-connection` for replacement options.
- The `connection` argument to `send_mail`, `send_mass_mail`, `mail_admins`, `mail_managers`, and `EmailMessage` is deprecated. The `EmailMessage.connection` attribute is also deprecated. […]
- The `fail_silently` argument to `send_mail`, `send_mass_mail`, `mail_admins`, `mail_managers`, and `EmailMessage.send` is deprecated. See `migrating-to-mailers-fail-silently` for alternatives.
- The `auth_user` and `auth_password` arguments to `send_mail` and `send_mass_mail` are deprecated. Replace them with `"username"` and `"password"` `OPTIONS` in `MAILERS`. See `migrating-to-mailers-auth`.
- Directly constructing and using instances of the `smtp.EmailBackend` class is deprecated. Use `mail.mailers` to obtain email backend instances.
- The `BaseEmailBackend.init()` constructor no longer silently ignores unknown keyword arguments. Custom email backend subclasses should ensure they have consumed all supported `kwargs` before forwarding the remainder to superclass […]
### 6.0 (2025-12-03) [source](https://github.com/django/django/blob/main/docs/releases/6.0.txt)
- Positional arguments in django.core.mail APIs: `django.core.mail` APIs now require keyword arguments for less commonly used parameters. […]
- All *optional* parameters (`fail_silently` and later) must be passed as keyword arguments to `get_connection`, `mail_admins`, `mail_managers`, `send_mail`, and `send_mass_mail`.
- All parameters must be passed as keyword arguments when creating an `EmailMessage` or `EmailMultiAlternatives` instance, except for the first four (`subject`, `body`, `from_email`, and `to`), which may still be passed either as […]
- (1 more in this category not shown; see the changelog.)

## Minimum versions and platform support
### 6.1 (2026-08-05) [source](https://github.com/django/django/blob/main/docs/releases/6.1.txt)
- Django 6.1 supports Python 3.12, 3.13, 3.14, and 3.15 (as of 6.1.3). We highly recommend, and only officially support, the latest release of each series.
### 6.0 (2025-12-03) [source](https://github.com/django/django/blob/main/docs/releases/6.0.txt)
- Django 6.0 supports Python 3.12, 3.13, and 3.14. We highly recommend, and only officially support, the latest release of each series.
- The Django 5.2.x series is the last to support Python 3.10 and 3.11.
- Following the release of Django 6.0, we suggest that third-party app authors drop support for all versions of Django prior to 5.2. […]
- Dropped support for Python < 3.12: Because Python 3.12 is now the minimum supported version for Django, any optional dependencies must also meet that requirement. […]

## New APIs and features
### 6.1 (2026-08-05) [source](https://github.com/django/django/blob/main/docs/releases/6.1.txt)
- Model field fetch modes: The on-demand fetching behavior of model fields is now configurable with `fetch modes`. These modes allow you to control how Django fetches data from the database when an unfetched field is accessed.
- `FETCH_ONE`, the default, fetches the missing field for the current instance only. This mode represents Django's existing behavior.
- `FETCH_PEERS` fetches a missing field for all instances that came from the same `django.db.models.query.QuerySet`.
- `FETCH_RAISE` raises a `django.core.exceptions.FieldFetchBlocked` exception.
- Fetch all books.
- Fetch associated authors.
- Database-level delete options for ForeignKey.on_delete: `ForeignKey.on_delete` now supports database-level delete options
- `django.db.models.DB_CASCADE`
### 6.0 (2025-12-03) [source](https://github.com/django/django/blob/main/docs/releases/6.0.txt)
- Template Partials: The `Django Template Language` now supports `template partials`, making it easier to encapsulate and reuse small named fragments within a template file. […]
- Background Tasks: Django now includes a built-in Tasks framework for running code outside the HTTP request–response cycle. This enables offloading work, such as sending emails or processing data, to background workers.
- Adoption of Python's modern email API: Email handling in Django now uses Python's modern email API, introduced in Python 3.6. This API, centered around the `email.message.EmailMessage` class, offers a cleaner and Unicode-friendly […]
- django.contrib.admin
- The Font Awesome Free icon set (version 6.7.2) is now used for the admin interface icons.
- The new `AdminSite.password_change_form` attribute allows customizing the form used in the admin site password change view.
- Message levels `messages.DEBUG` and `messages.INFO` now have distinct icons and CSS styling. Previously, both levels shared the same appearance as `messages.SUCCESS`. […]
- django.contrib.auth
- (97 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 48 releases; 2 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 6.1.3, 6.1.2, 6.1.1, 6.0.10, 6.0.9, 6.0.8, 6.0.7, 6.0.6, 6.0.5, 6.0.4, 6.0.3, 6.0.2 and 34 more.
- Sources: https://raw.githubusercontent.com/django/django/main/docs/releases/{version}.txt; registry (pypi) for dates.
