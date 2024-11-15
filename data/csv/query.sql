SELECT
  campus.name,
  curso.name,
  disciplina.name,
  exercicio.horario,
  exercicio.semestre
FROM
  campus,
  curso,
  disciplina,
  exercicio
WHERE
  campus.id = exercicio.campus
  AND
  curso.id = exercicio.curso
  AND
  disciplina.id = exercicio.disciplina
  AND
  exercicio.campus = 3
  AND
  exercicio.horario regexp '^[0-9]{2,3}m[0-9]{2,3}$'
  AND
  exercicio.semestre = '2024_2'
;
