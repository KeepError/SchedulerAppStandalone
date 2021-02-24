import sys
import sqlite3
from datetime import datetime, timedelta

# from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QColor, QGuiApplication
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog

from ui import main_widget
from ui import info_dialog, warning_dialog
from ui import edit_group_dialog, edit_task_dialog, add_many_tasks_dialog, add_week_day_dialog
from ui import show_task_dialog


class WarningDialog(QDialog, warning_dialog.Ui_Dialog):
    def __init__(self, parent, window_title, text):
        """Инициализация диалогового окна"""
        super().__init__(parent)
        # uic.loadUi('warning_dialog.ui', self)
        self.setupUi(self)
        self.setWindowTitle(window_title)

        self.label_warning.setText(text)

        self.btn_yes.clicked.connect(self.accept)
        self.btn_no.clicked.connect(self.reject)


class InfoDialog(QDialog, info_dialog.Ui_Dialog):
    def __init__(self, parent, window_title, text):
        """Инициализация диалогового окна"""
        super().__init__(parent)
        # uic.loadUi('info_dialog.ui', self)
        self.setupUi(self)
        self.setWindowTitle(window_title)

        self.label_info.setText(text)

        self.btn_ok.clicked.connect(self.accept)


class EditGroupDialog(QDialog, edit_group_dialog.Ui_Dialog):
    def __init__(self, parent, window_title):
        """Инициализация диалогового окна"""
        super().__init__(parent)
        # uic.loadUi('edit_group_dialog.ui', self)
        self.setupUi(self)
        self.setWindowTitle(window_title)

        self.check_type()

        self.buttonBox.accepted.connect(self.ok_pressed)
        self.combo_type.currentIndexChanged.connect(self.check_type)

    def check_type(self):
        """Проверка типа группы и отключение виджетов"""
        if self.combo_type.currentIndex() == 0:
            self.check_deletePast.setDisabled(True)
            self.check_deletePast.setChecked(False)
        else:
            self.check_deletePast.setDisabled(False)

    def check_form(self):
        """Проверка формы на корректность"""
        if not self.edit_title.text():
            return False
        return True

    def ok_pressed(self):
        """Функция-слот нажатия ОК"""
        if not self.check_form():
            return self.label_info.setText('Неверно заполнена форма')
        self.accept()

    def set_group(self, group):
        """Заполнение полей формы"""
        self.edit_title.setText(str(group['title']))
        self.edit_description.setText(str(group['description']))
        self.check_deletePast.setChecked(bool(group['delete_past']))
        self.combo_type.setCurrentIndex(group['type'])

        self.label_type.hide()
        self.combo_type.hide()

    def get_title(self):
        """Получение введенного названия группы"""
        return str(self.edit_title.text())

    def get_description(self):
        """Получение введенного описания группы"""
        return str(self.edit_description.text())

    def get_type(self):
        """Получение выбранного типа группы"""
        return self.combo_type.currentIndex()

    def get_delete_past(self):
        """Получение значения чекбокса удаления предыдущих задач"""
        return int(self.check_deletePast.isChecked())


class EditTaskDialog(QDialog, edit_task_dialog.Ui_Dialog):
    def __init__(self, parent, window_title):
        """Инициализация диалогового окна"""
        super().__init__(parent)
        # uic.loadUi('edit_task_dialog.ui', self)
        self.setupUi(self)
        self.setWindowTitle(window_title)

        self.image_path = None
        self.check_image()

        now = datetime.now()
        self.dateEdit.setDateTime(now)

        self.buttonBox.accepted.connect(self.ok_pressed)
        self.btn_selectImage.clicked.connect(self.select_image)
        self.btn_deleteImage.clicked.connect(self.delete_image)

    def check_group_type(self, group_type):
        """Проверка типа группы и отключение виджетов"""
        disabled = [
            (self.dateEdit, self.timeEdit),
            (self.timeEdit,),
            ()
        ]
        for widget in disabled[group_type]:
            widget.setDisabled(True)

    def check_form(self):
        """Проверка формы на корректность"""
        if not self.edit_title.text():
            return False
        return True

    def ok_pressed(self):
        """Функция-слот нажатия ОК"""
        if not self.check_form():
            return self.label_info.setText('Неверно заполнена форма')
        self.accept()

    def check_image(self):
        """Проверка наличия изображения и отключение кнопки удаления"""
        if self.image_path:
            self.label_imageName.setText(self.image_path.split('/')[-1])
            self.btn_deleteImage.setDisabled(False)
        else:
            self.label_imageName.setText('')
            self.btn_deleteImage.setDisabled(True)

    def select_image(self):
        """Функция-слот нажатия на кнопку выбора изображения"""
        path = QFileDialog.getOpenFileName(self, 'Выбрать изображение',
                                           '', 'Изображение (*.jpg *jpeg *png)')[0]
        if not path:
            self.image_path = None
            return
        self.image_path = path
        self.check_image()

    def delete_image(self):
        """Функция-слот нажатия на кнопку удаления изображения"""
        self.image_path = None
        self.check_image()

    def set_task(self, task):
        """Заполнение полей формы"""
        self.check_group_type(task['group']['type'])

        self.edit_title.setText(str(task['title']))
        self.edit_description.setPlainText(str(task['description']))
        if task['image']:
            self.image_path = task['image']
            self.check_image()
        self.dateEdit.setDateTime(task['datetime'])
        self.timeEdit.setDateTime(task['datetime'])

    def get_title(self):
        """Получение введенного названия задачи"""
        return str(self.edit_title.text())

    def get_description(self):
        """Получение введенного описания задачи"""
        return str(self.edit_description.toPlainText())

    def get_image(self):
        """Получение выбранного изображения задачи"""
        return self.image_path

    def get_datetime(self):
        """Получение выбранных даты и времени задачи"""
        date = self.dateEdit.date()
        time = self.timeEdit.time()
        dt = datetime(date.year(), date.month(), date.day(), time.hour(), time.minute())
        return dt


class ShowTaskDialog(QDialog, show_task_dialog.Ui_Dialog):
    def __init__(self, parent, task):
        """Инициализация диалогового окна"""
        super().__init__(parent)
        # uic.loadUi('show_task_dialog.ui', self)
        self.setupUi(self)
        self.setWindowTitle('Информация о задаче')

        self.image_size = (300, 300)
        self.window_size_without_image = (430, 360)

        self.init_task(task)

    def init_task(self, task):
        """Инициализация задачи"""
        self.edit_title.setText(str(task['title']))

        if not task['description']:
            self.edit_description.setPlainText('Отсутствует')
        else:
            self.edit_description.setPlainText(str(task['description']))

        dt = task['dt_string']
        if not dt:
            self.label_datetime.hide()
            self.edit_datetime.hide()
        else:
            self.edit_datetime.setText(dt)

        if task['image'] is None:
            return self.resize(*self.window_size_without_image)
        pixmap = QPixmap(task['image']).scaled(*self.image_size, Qt.KeepAspectRatio)
        self.image.setPixmap(pixmap)


class AddManyTasksDialog(QDialog, add_many_tasks_dialog.Ui_Dialog):
    def __init__(self, parent, group):
        """Инициализация диалогового окна"""
        super().__init__(parent)
        # uic.loadUi('add_many_tasks_dialog.ui', self)
        self.setupUi(self)
        self.setWindowTitle('Добавить несколько задач')

        self.week_days = []

        self.group = group
        self.check_group()

        self.week_day_names = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
                               'Пятница', 'Суббота', 'Воскресенье']

        self.check_edit_week_day_buttons()

        now = datetime.now()
        self.edit_date.setDateTime(now)
        if group['type'] > 1:
            self.edit_time.setDateTime(now)

        self.buttonBox.accepted.connect(self.ok_pressed)
        self.btn_addWeekDay.clicked.connect(self.add_week_day)
        self.btn_deleteWeekDay.clicked.connect(self.delete_week_day)
        self.list_weekDays.currentRowChanged.connect(self.check_edit_week_day_buttons)

    def check_group(self):
        """Проверка группы и скрытие виджетов"""
        group_type = self.group['type']
        if group_type == 0:
            self.label_weekDays.hide()
            self.list_weekDays.hide()
            self.btn_addWeekDay.hide()
            self.btn_deleteWeekDay.hide()

            self.label_startDate.hide()
            self.edit_date.hide()
            self.edit_time.hide()

        elif group_type == 1:
            self.edit_time.hide()

    def check_edit_week_day_buttons(self):
        """Функция-слот нажатия на кнопку выбора дня недели"""
        is_selected = self.list_weekDays.currentRow() in range(len(self.week_days))
        self.btn_deleteWeekDay.setDisabled(not is_selected)

    def update_week_days_list(self):
        """Обновление виджета списка дней недели"""
        self.list_weekDays.clear()
        for item in self.week_days:
            time = f' - {item["hour"]:02}:{item["minute"]:02}' if self.group['type'] > 1 else ''
            result = self.week_day_names[item['week_day']] + time
            self.list_weekDays.addItem(result)

    def add_week_day(self):
        """Функция-слот нажатия на кнопку добавления дня недели"""
        dialog = AddWeekDayDialog(self)
        dialog.update_week_day_names(self.week_day_names)
        dialog.check_group(self.group)

        is_ok = dialog.exec_()
        if not is_ok:
            return

        self.week_days.append(dialog.get_data())
        self.update_week_days_list()

    def delete_week_day(self):
        """Функция-слот нажатия на кнопку удаления дня недели"""
        index = self.list_weekDays.currentRow()
        if index not in range(len(self.week_days)):
            return

        self.week_days.pop(index)
        self.update_week_days_list()
        self.list_weekDays.setCurrentRow(len(self.week_days) - 1)

    def get_task_titles(self):
        """Получение введенных названий задач"""
        titles = self.edit_tasks.toPlainText().split('\n')
        return list(filter(lambda s: s.strip(), titles))

    def get_tasks(self):
        """Получение добавленных задач"""
        week_days = self.week_days
        task_titles = self.get_task_titles()

        dates = []

        selected_date = self.edit_date.date()
        selected_time = self.edit_time.time()

        current_date = datetime(selected_date.year(), selected_date.month(), selected_date.day(),
                                selected_time.hour(), selected_time.minute())

        if self.group['type'] == 0:
            return [(title, current_date) for title in task_titles]

        index = 0
        while len(dates) < len(task_titles):
            week_day = week_days[index]
            current_time = current_date.hour * 100 + current_date.minute
            needed_time = week_day['hour'] * 100 + week_day['minute']
            if current_date.weekday() == week_day['week_day'] and needed_time >= current_time:
                current_date = current_date.replace(hour=week_day['hour'], minute=week_day['minute'])
                dates.append(current_date)
                index += 1
                if index > len(week_days) - 1:
                    index = 0
                    current_date += timedelta(minutes=1)
            else:
                current_date += timedelta(days=1)
                current_date = current_date.replace(hour=0, minute=0)

        return [(task_titles[i], dates[i]) for i in range(len(task_titles))]

    def check_form(self):
        """Проверка формы на корректность"""
        if not self.get_task_titles() or (not self.week_days and self.group['type'] >= 1):
            return False
        return True

    def ok_pressed(self):
        """Функция-слот нажатия ОК"""
        if not self.check_form():
            return self.label_info.setText('Неверно заполнена форма')
        self.accept()


class AddWeekDayDialog(QDialog, add_week_day_dialog.Ui_Dialog):
    def __init__(self, parent):
        """Инициализация диалогового окна"""
        super().__init__(parent)
        # uic.loadUi('add_week_day_dialog.ui', self)
        self.setupUi(self)
        self.setWindowTitle('Добавить день недели')

    def update_week_day_names(self, week_day_names):
        """Обновит названия дней недели"""
        self.select_weekDay.clear()
        self.select_weekDay.addItems(week_day_names)

    def check_group(self, group):
        """Проверка группы и скрытие виджетов"""
        if group['type'] <= 1:
            self.label_time.hide()
            self.edit_time.hide()

    def get_data(self):
        """Получение данных"""
        time = self.edit_time.time()
        data = {
            'week_day': self.select_weekDay.currentIndex(),
            'hour': time.hour(),
            'minute': time.minute()
        }
        return data


class MainWidget(QMainWindow, main_widget.Ui_MainWindow):
    def __init__(self):
        """Инициализация главного окна"""
        super().__init__()
        # uic.loadUi('main_widget.ui', self)
        self.setupUi(self)
        self.setWindowTitle('Планировщик')

        self.default_groups = [
            {
                'title': 'Сегодня',
                'description': 'Задачи, спланированные на сегодняшний день',
                'filter_func': lambda task: task['datetime'].date() == datetime.now().date() and
                                            task['group']['type'] != 0
            },
            {
                'title': 'Избранное',
                'description': 'Задачи, помеченные как избранные',
                'filter_func': lambda task: task['favorite'] == 1
            },
            {
                'title': '-' * 39
            }
        ]

        self.group_type_datetime_format = [
            lambda dt: '',
            lambda dt: dt.strftime('%d.%m.%Y'),
            lambda dt: dt.strftime('%d.%m.%Y %H:%M')
        ]

        self.connection = sqlite3.connect('scheduler.db', detect_types=sqlite3.PARSE_COLNAMES)
        self.connection.execute('PRAGMA foreign_keys = ON')

        self.update_groups()
        self.list_groups.setCurrentRow(0)
        self.update_tasks()
        self.group_selected()

        self.list_groups.itemDoubleClicked.connect(self.update_tasks)
        self.list_groups.currentRowChanged.connect(self.group_selected)
        self.btn_createGroup.clicked.connect(self.create_group)
        self.btn_editGroup.clicked.connect(self.edit_group)
        self.btn_deleteGroup.clicked.connect(self.delete_group)

        self.list_tasks.currentRowChanged.connect(self.task_selected)
        self.btn_addTask.clicked.connect(self.add_task)
        self.btn_editTask.clicked.connect(self.edit_task)
        self.btn_deleteTask.clicked.connect(self.delete_task)
        self.check_favorite.clicked.connect(self.change_favorite_state)
        self.list_tasks.itemDoubleClicked.connect(self.load_task)
        self.btn_copyTasks.clicked.connect(self.copy_tasks_to_clipboard)
        self.btn_copyDates.clicked.connect(self.copy_dates_to_clipboard)
        self.btn_addManyTasks.clicked.connect(self.add_many_tasks)

    def execute_result_tuple_to_dict(self, result):
        """Преобразование полученного объекта из базы данных в словарь"""
        titles = [item[0] for item in result.description]
        res = result.fetchall()
        return [{titles[j]: item[j] for j in range(len(titles))} for item in res]

    def get_groups(self):
        """Получение групп из базы данных"""
        query = 'SELECT * FROM Groups'
        result = self.connection.cursor().execute(query)
        groups = self.execute_result_tuple_to_dict(result)

        result_groups = self.default_groups[:]
        for group in groups:
            new_group = group.copy()
            new_group['filter_func'] = lambda task, group_id=group['id']: \
                task['group_id'] == group_id
            new_group['is_custom'] = True
            result_groups.append(new_group)

        return result_groups

    def get_tasks(self):
        """Получение задач из базы данных"""
        def get_group(group_id):
            for group in self.groups:
                if group_id == group.get('id', None):
                    return group

        query = """
        SELECT id, title, description as "description [string]", group_id, 
        datetime as "datetime [timestamp]", favorite, image FROM Tasks
        """
        result = self.connection.cursor().execute(query)
        tasks = self.execute_result_tuple_to_dict(result)
        for task in tasks:
            task['group'] = get_group(task['group_id'])
            task['dt_string'] = self.group_type_datetime_format[task['group']['type']]\
                (task['datetime'])
        return tasks

    def get_group_from_list(self):
        """Получение выбранной в виджете группы"""
        index = self.list_groups.currentRow()
        if index not in range(len(self.groups)):
            return

        group = self.groups[index]
        if group.get('filter_func', None) is None:
            return

        return group

    def update_groups(self):
        """Обновление групп в виджете"""
        self.groups = self.get_groups()
        tasks = self.get_tasks()

        self.list_groups.clear()
        for group in self.groups:
            if group.get('filter_func', None) is None:
                item = group['title']
            else:
                length = len(list(filter(group['filter_func'], tasks)))
                item = f'[{length}] {group["title"]}'
            self.list_groups.addItem(item)

    def update_tasks(self):
        """Обновление задач в виджете"""
        def delete_past_tasks(tasks):
            """Удаление прошедших задач"""
            ids = []
            dt_now = datetime.now()
            for task in tasks:
                if task['group']['type'] >= 1 and task['group']['delete_past'] == 1 and \
                        task['datetime'] < dt_now:
                    ids.append(task['id'])

            if not ids:
                return tasks

            query = f"""
            DELETE FROM Tasks
            WHERE id in ({','.join(map(str, ids))})
            """
            self.connection.cursor().execute(query)
            self.connection.commit()

            self.update_groups()

            return list(filter(lambda task: task['id'] not in ids, tasks))

        group = self.get_group_from_list()
        if group is None:
            return

        group_title = str(group['title'])
        group_description = str(group['description']) if group['description'] \
            else 'Описание не задано'
        self.label_groupTitle.setText(group_title)
        self.edit_groupDescription.setText(group_description)

        self.list_tasks.clear()

        tasks = list(filter(group['filter_func'], self.get_tasks()))
        tasks = delete_past_tasks(tasks)
        tasks.sort(key=lambda task: (task['group']['type'] == 0, task['datetime']))

        rows = []
        for task in tasks:
            dt = task['dt_string']
            if dt:
                dt = f'[{dt}] '
            rows.append(dt + str(task['title']))
        self.list_tasks.addItems(rows)

        for row, task in enumerate(tasks):
            if task['favorite']:
                self.list_tasks.item(row).setBackground(QColor(255, 241, 148))

        if not rows:
            self.list_tasks.addItem('Задачи отсутствуют')

        self.check_favorite.setChecked(False)

        self.loaded_group_index = self.list_groups.currentRow()
        self.loaded_tasks = tasks[:]

        self.task_selected()

    def group_selected(self):
        """Функция-слот клика по группе"""
        def change_edit_state(disabled):
            """Отключение виджетов"""
            self.btn_editGroup.setDisabled(disabled)
            self.btn_deleteGroup.setDisabled(disabled)

        index = self.list_groups.currentRow()
        if index not in range(len(self.groups)):
            return change_edit_state(True)

        group = self.groups[index]

        if not group.get('is_custom'):
            return change_edit_state(True)

        change_edit_state(False)

    def task_selected(self):
        """Функция слот клика по задаче"""
        def change_edit_state(disabled):
            """Отключение виджетов"""
            self.btn_editTask.setDisabled(disabled)
            self.btn_deleteTask.setDisabled(disabled)
            self.check_favorite.setDisabled(disabled)

        edit_state = False
        add_task_button_state = False

        if self.loaded_group_index not in range(len(self.groups)) or \
                not self.groups[self.loaded_group_index].get('is_custom'):
            add_task_button_state = True

        index = self.list_tasks.currentRow()
        if index not in range(len(self.loaded_tasks)):
            edit_state = True
        else:
            task = self.loaded_tasks[index]
            self.check_favorite.setChecked(bool(task['favorite']))

        self.btn_addTask.setDisabled(add_task_button_state)
        self.btn_addManyTasks.setDisabled(add_task_button_state)
        change_edit_state(edit_state)

    def create_group(self):
        """Функция слот нажатия на кнопку добавления группы"""
        dialog = EditGroupDialog(self, 'Создать группу')

        is_ok = dialog.exec_()
        if not is_ok:
            return

        query = """
        INSERT INTO Groups (title, description, type, delete_past)
        VALUES (?, ?, ?, ?)
        """
        self.connection.cursor().execute(query, (dialog.get_title(), dialog.get_description(),
                                                 dialog.get_type(), dialog.get_delete_past()))
        self.connection.commit()

        self.update_groups()
        self.list_groups.setCurrentRow(len(self.groups) - 1)
        self.update_tasks()

    def edit_group(self):
        """Функция слот нажатия на кнопку редактирования группы"""
        index = self.list_groups.currentRow()

        group = self.get_group_from_list()

        dialog = EditGroupDialog(self, 'Редактировать группу')

        dialog.set_group(group)

        is_ok = dialog.exec_()
        if not is_ok:
            return

        query = """
        UPDATE Groups
        SET title = ?, description = ?, delete_past = ?
        WHERE id = ?
        """

        self.connection.cursor().execute(query, (dialog.get_title(), dialog.get_description(),
                                                 dialog.get_delete_past(), group['id']))
        self.connection.commit()

        self.update_groups()
        self.list_groups.setCurrentRow(index)
        self.update_tasks()

    def delete_group(self):
        """Функция слот нажатия на кнопку удаления группы"""
        group = self.get_group_from_list()

        dialog = WarningDialog(self, 'Удалить группу', 'Вы уверены, что хотите удалить группу?')

        is_ok = dialog.exec_()
        if not is_ok:
            return

        query = """
        DELETE FROM Groups
        WHERE id = ?
        """

        self.connection.cursor().execute(query, (group['id'],))
        self.connection.commit()

        self.update_groups()
        self.list_groups.setCurrentRow(0)
        self.update_tasks()

    def add_task(self):
        """Функция слот нажатия на кнопку добавления задачи"""
        group = self.groups[self.loaded_group_index]

        dialog = EditTaskDialog(self, 'Добавить задачу')
        dialog.check_group_type(group['type'])

        is_ok = dialog.exec_()
        if not is_ok:
            return

        query = """
        INSERT INTO Tasks (title, description, group_id, datetime, image)
        VALUES (?, ?, ?, ? ,?)
        """
        params = (dialog.get_title(), dialog.get_description(), group['id'],
                  dialog.get_datetime(), dialog.get_image())
        self.connection.cursor().execute(query, params)
        self.connection.commit()

        self.update_groups()
        self.list_groups.setCurrentRow(self.loaded_group_index)
        self.update_tasks()

    def edit_task(self):
        """Функция слот нажатия на кнопку редактирования задачи"""
        task = self.loaded_tasks[self.list_tasks.currentRow()]

        dialog = EditTaskDialog(self, 'Редактировать задачу')

        dialog.set_task(task)

        is_ok = dialog.exec_()
        if not is_ok:
            return

        query = """
        UPDATE Tasks
        SET title = ?, description = ?, group_id = ?, datetime = ?, image = ?
        WHERE id = ?
        """
        params = (dialog.get_title(), dialog.get_description(), task['group']['id'],
                  dialog.get_datetime(), dialog.get_image(), task['id'])
        self.connection.cursor().execute(query, params)
        self.connection.commit()

        self.update_groups()
        self.list_groups.setCurrentRow(self.loaded_group_index)
        self.update_tasks()

    def delete_task(self):
        """Функция слот нажатия на кнопку удаления задачи"""
        task = self.loaded_tasks[self.list_tasks.currentRow()]

        dialog = WarningDialog(self, 'Удалить задачу', 'Вы уверены, что хотите удалить задачу?')

        is_ok = dialog.exec_()
        if not is_ok:
            return

        query = """
        DELETE FROM Tasks
        WHERE id = ?
        """

        self.connection.cursor().execute(query, (task['id'],))
        self.connection.commit()

        self.update_groups()
        self.list_groups.setCurrentRow(self.loaded_group_index)
        self.update_tasks()

    def change_favorite_state(self):
        """Функция слот добавления/удаления задачи в избранное"""
        group = self.groups[self.loaded_group_index]
        if group is None:
            return

        if self.list_tasks.currentRow() not in range(len(self.loaded_tasks)):
            return

        task = self.loaded_tasks[self.list_tasks.currentRow()]

        query = """
        UPDATE Tasks
        SET favorite = ?
        WHERE id = ?
        """
        params = (self.check_favorite.isChecked(), task['id'])
        self.connection.cursor().execute(query, params)
        self.connection.commit()

        self.update_groups()
        self.list_groups.setCurrentRow(self.loaded_group_index)
        self.update_tasks()

    def load_task(self):
        """Функция-слот двойного клика по задаче"""
        group = self.groups[self.loaded_group_index]
        if group is None:
            return

        if self.list_tasks.currentRow() not in range(len(self.loaded_tasks)):
            return

        task = self.loaded_tasks[self.list_tasks.currentRow()]

        dialog = ShowTaskDialog(self, task)

        dialog.exec_()

    def copy_tasks_to_clipboard(self):
        """Функция слот нажатия на кнопку копирования задач (с датой и временем)"""
        result = []
        for task in self.loaded_tasks:
            if task['dt_string']:
                result.append(task['dt_string'] + ' - ' + str(task['title']))
            else:
                result.append(str(task['title']))

        if not result:
            dialog = InfoDialog(self, 'Ошибка', 'Задачи отсутствуют')
            return dialog.exec_()
        cb = QGuiApplication.clipboard()
        cb.setText('\n'.join(result), mode=cb.Clipboard)
        dialog = InfoDialog(self, 'Успех', 'Задачи скопированы в буфер обмена')
        dialog.exec_()

    def copy_dates_to_clipboard(self):
        """Функция слот нажатия на кнопку копирования задач (без даты и времени)"""
        result = [task['dt_string'] for task in self.loaded_tasks]

        if not result:
            dialog = InfoDialog(self, 'Ошибка', 'Задачи отсутствуют')
            return dialog.exec_()
        cb = QGuiApplication.clipboard()
        cb.setText('\n'.join(result), mode=cb.Clipboard)
        dialog = InfoDialog(self, 'Успех', 'Даты скопированы в буфер обмена')
        dialog.exec_()

    def add_many_tasks(self):
        """Функция-слот нажатия на кнопку добавления нескольких задач"""
        group = self.groups[self.loaded_group_index]
        dialog = AddManyTasksDialog(self, group)

        is_ok = dialog.exec_()
        if not is_ok:
            return

        data = dialog.get_tasks()

        query = "INSERT INTO Tasks(title,description,datetime,group_id) VALUES" + \
                ",".join(["(?,'',?,?)"] * len(data))

        values = []
        for item in data:
            values += [item[0], item[1], group['id']]

        self.connection.cursor().execute(query, tuple(values))
        self.connection.commit()

        self.update_groups()
        self.list_groups.setCurrentRow(self.loaded_group_index)
        self.update_tasks()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    ex = MainWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
