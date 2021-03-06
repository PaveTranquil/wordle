# Формат коммита
### <тип>[контекст]: <заголовок>
Тело коммита с описью в виде списка и по файлам, если изменения в нескольких файлах сразу. <br>
Refs: [сноски на pull requests и issues, при их наличии]

## Примеры:
#### [3828fa7](https://github.com/PaveTranquil/wordle/commit/3828fa7b5ed7445060e8d267100af6f55130ae23)
> **fix: добавлена проверка на аббревиатуры** <br><br>
> functions.py → get_new_word() <br>
>⠀- Добавлен тип «сокращённое» в исключения из списка <br>
>⠀- Приведение к нижнему регистру возвращаемого слова <br><br>
> main.py <br>
>⠀- Приведение к нижнему регистру слова, которое вводит юзер

#### [2ab1593](https://github.com/PaveTranquil/wordle/commit/2ab159334808b928d5b2678b2cc9746b015674d0)
> **refactor: подготовка админ-панели к изменениям** <br><br>
> settings.py <br>
> ⠀- ADMIN преобразован в список, содержащий ID админов <br><br>
> main.py <br>
> ⠀- Правка кода в соответствии с изменением выше


# Типы коммитов
- init — начало задачи, старт реализации
- feat — реализация фичи
- refeat — изменение фичи
- update — обновление кода под последние изменения
- fix — исправление ошибок
- refactor — рефакторинг, изменение кода без изменения функционала
- style	— правки по кодстайлу
- docs — документация к проекту
- revert — откаты на предыдущие коммиты

# Ограничения
- Заголовок коммита ≤ 60 символов
- Строка тела коммита ≤ 82 символа
