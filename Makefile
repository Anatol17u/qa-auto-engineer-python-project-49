# Makefile
install: # Устанавливает и удаляет пакеты: приводит зависимости в виртуальном окружении 
	uv sync

brain-games: # Запускаем игру
	uv run brain-games

build: # Собираем проект/ Выполняет сборку новой версии пакета
	uv build

package-install: # Устанавливаем пакет в операционную систему
	uv tool install dist/*.whl

lint: # Проверяем на ошибки
	uv run ruff check brain_games
brain-even: # Запускаем игру 
	uv run brain-even
brain-calc:
	uv run brain-calc
brain-gcd:
	uv run brain-gcd
brain-progression:
	uv run brain-progression