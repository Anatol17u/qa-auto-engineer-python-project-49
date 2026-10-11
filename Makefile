# Makefile
install: # Устанавливает и удаляет пакеты: приводит зависимости в виртуальном окружении 
	uv sync

brain-games: # Запускаем игру
	uv run brain-games

build: # Собираем проект
	uv build

package-install: # Устанавливаем пакет в операционную систему
	uv tool install dist/*.whl
