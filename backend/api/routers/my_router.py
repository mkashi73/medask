class MyRouter:
    route_app_labels = {
        'admin',
        'auth',
        'contenttypes',
        'sessions',
        'messages',
        'staticfiles',
        'rest_framework',
        'token_blacklist',
        'django_filters',
        'corsheaders',
        'api',
    }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'default'
        return None



class JPARouter:
    route_app_labels = {        
        'jpa'
    }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'jpa_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'jpa_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'jpa_db'
        return None


        
