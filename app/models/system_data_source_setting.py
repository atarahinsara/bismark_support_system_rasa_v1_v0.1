from app.extensions import db

class SystemDataSourceSetting(db.Model):
    __tablename__ = 'system_data_source_settings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    setting_key = db.Column(db.String(50), unique=True, nullable=False)
    setting_value = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<SystemDataSourceSetting(key={self.setting_key}, value={self.setting_value})>"


class SystemDataSourceSettingManager:
    @staticmethod
    def get_setting(key: str, default: str = None) -> str:
        setting = SystemDataSourceSetting.query.filter_by(setting_key=key).first()
        return setting.setting_value if setting else default

    @staticmethod
    def set_setting(key: str, value: str, description: str = None) -> SystemDataSourceSetting:
        setting = SystemDataSourceSetting.query.filter_by(setting_key=key).first()
        if setting:
            setting.setting_value = value
            if description:
                setting.description = description
        else:
            setting = SystemDataSourceSetting(setting_key=key, setting_value=value, description=description)
            db.session.add(setting)
        db.session.commit()
        return setting

    @staticmethod
    def delete_setting(key: str) -> bool:
        setting = SystemDataSourceSetting.query.filter_by(setting_key=key).first()
        if setting:
            db.session.delete(setting)
            db.session.commit()
            return True
        return False
