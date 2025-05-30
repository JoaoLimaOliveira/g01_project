from flask import render_template, session
from classes.course import Course
from classes.department import Department
from datafile import filename
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import os

def apps_plotly():
    try:
        # Caminho correto do banco de dados
        db_path = os.path.join(filename, 'business.db')
        engine = create_engine(f'sqlite:///{db_path}')
        df_coursestudent = pd.read_sql('Course_Student', con=engine)

        # Mapeamento das notas por letra
        grade_map = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}
        df_coursestudent['grade_numeric'] = df_coursestudent['grade'].map(grade_map)
        df_coursestudent = df_coursestudent.dropna(subset=['grade_numeric'])

        # Criar uma nova coluna com o departments_id
        df_coursestudent['departments_id'] = df_coursestudent['courses_id'].apply(
            lambda cid: Course.obj[cid].departments_id if cid in Course.obj else None
        )
        df_coursestudent = df_coursestudent.dropna(subset=['departments_id'])

        # Calcular média de notas por departamento
        result = df_coursestudent.groupby('departments_id')['grade_numeric'].mean().round(2)

        # Obter nomes dos departamentos
        department_names = []
        for dept_id in result.index:
            dept_obj = Department.obj.get(dept_id)
            department_names.append(dept_obj.department_name if dept_obj else f"Department {dept_id}")
            
        df_plot = pd.DataFrame({
            'Department': department_names,
            'Average Grade': result.values   
        })
        
        fig = px.bar(
            df_plot,
            x='Department',
            y='Average Grade',
            labels={'Department': 'Department', 'Average Grade': 'Average Grade (Numeric)'},
            title='Average Grades by Department',
            color='Average Grade',
            color_continuous_scale='Blues',
            range_y=[0, 5]
        )
        
    

        
        plot_div = fig.to_html(full_html=False)
        return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))

    except Exception as e:
        return f"Erro: {e}"




