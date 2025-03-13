# Flujo de Trabajo Git

1. Siempre crear rama para nuevas características:
   ```bash
   git checkout -b feature/nueva-caracteristica
   ```

2. Hacer commits pequeños y descriptivos:
   ```bash
   git commit -m "Agregada validación de campos en formulario"
   ```

3. Probar antes de fusionar:
   ```bash
   # Ejecutar pruebas
   pytest
   
   # Si pasan, fusionar
   git checkout main
   git merge feature/nueva-caracteristica
   ```

4. Crear tag para versiones estables:
   ```bash
   git tag -a v0.1.1 -m "Correcciones en validaciones"
   ```

5. Si algo falla, revertir:
   ```bash
   # Volver al último commit estable
   git reset --hard HEAD~1
   
   # O volver a una versión específica
   git checkout v0.1.0
   ``` 