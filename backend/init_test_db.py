import db.db_classes as db
from db.db_classes import (
    connect_db,
    ProfessionsTable,
    CoursesTable,
    SingletonConnection,
)
from pydantic import BaseModel


class Profession:
    def __init__(self, name: str) -> None:
        self.name = name
        self.description = "description of profession: " + name


def clear_db(conn: SingletonConnection) -> None:
    users = conn.session.query(db.UsersTable).all()
    login = conn.session.query(db.LoginDataTable).all()
    cours = conn.session.query(db.CoursesTable).all()
    proff = conn.session.query(db.ProfessionsTable).all()
    favor = conn.session.query(db.FavouritesTable).all()
    for row in users:
        conn.session.delete(row)
    for row in login:
        conn.session.delete(row)
    for row in cours:
        conn.session.delete(row)
    for row in proff:
        conn.session.delete(row)
    for row in favor:
        conn.session.delete(row)
    conn.session.commit()


conn = connect_db()
clear_db(conn)
proff = [
    "Архитектор",
    "Строитель",
    "Риэлтор",
    "Ландшафтный дизайнер",
    "Ландшафтный архитектор",
    "Ученый",
    "Археолог",
    "Научный сотрудник",
    "Учитель",
    "Библиотекарь",
    "Менеджер по проектам",
    "Экономист",
    "Исполнительный директор",
    "Консультант по управлению",
    "Сисадмин",
    "Программист",
    "Специалист по кибербезопасности",
    "Аналитик данных",
    "Инженер по тестированию ПО",
    "Врач",
    "Фармацевт",
    "Физиотерапевт",
    "Нутрициолог",
    "Психотерапевт",
    "Финансовый аналитик",
    "Бухгалтер",
    "Инвестиционный аналитик",
    "Финансовый консультант",
    "Аудитор",
    "Технолог в машиностроении",
    "Инженер-механик",
    "Робототехник",
    "Монтажник оборудования",
    "Военный офицер",
    "Солдат",
    "Военный медик",
    "Инженер-исследователь",
    "Научный исследователь",
    "Биолог",
    "Физик",
    "Химик",
    "Менеджер по продажам",
    "Продавец-консультант",
    "Кассир",
    "Рабочий на производстве",
    "Технолог по текстилю",
    "Швея",
    "Дизайнер легкой промышленности",
    "Маркетолог",
    "Рекламщик",
    "Рукрутер",
    "Менеджер по продукту",
    "Водитель",
    "Логист",
    "Пилот",
    "Диспетчер",
    "Официант",
    "Парикмахер",
    "Мастер маникюра",
    "Бровист, Визажист",
    "Массажист",
    "Клининговая служба",
    "Гостиничный администратор",
    "Тур-агент",
    "Инженер по электронике и схемотехнике",
    "Инженер по проектированию микросхем",
    "Специалист по радиоэлектронике",
    "Художник",
    "Музыкант",
    "Режиссер",
    "Литературный редактор",
    "Спортивный тренер",
    "Професиональнй спортсмен",
    "Спортивный журналист",
    "Адвокат",
    "Судья",
    "Юрист корпорации",
    "Криминалист",
    "Фермер",
    "Агроном",
]
prof_data = list(map(lambda x: Profession(x), proff))
for i in prof_data:
    prof_unit = ProfessionsTable(name=i.name, description=i.description)
    conn.session.add(prof_unit)
    print(prof_unit.id)
    conn.session.commit()
    print(prof_unit.id)
    for i in range(3):
        course_unit = CoursesTable(
            course_name=f"course №{i} for profession {prof_unit.name}",
            description="some description for course",
            profession_id=prof_unit.id,
        )
        conn.session.add(course_unit)
        conn.session.commit()
        print(
            course_unit.course_name, course_unit.description, course_unit.profession_id
        )
conn.session.commit()
conn.session.add(db.UsersTable(id=1, name="TestUser1"))
conn.session.add(db.LoginDataTable(login="1", password="1", user_id=1))
conn.session.commit()
conn.session.add(
    db.UsersTable(id=2, name="Alex", vk_id="2332132", access_token="afdjklajfk")
)
conn.session.add(
    db.UsersTable(id=3, name="dmitriy", vk_id="31232", access_token="jldaf")
)
conn.session.add(db.LoginDataTable(login="Alex", password="ILoveMath", user_id=2))
conn.session.add(db.LoginDataTable(login="dmitriy", password="ILoveMath", user_id=3))
conn.session.commit()
# https://www.youtube.com/watch?v=jfgNz4s99IA
