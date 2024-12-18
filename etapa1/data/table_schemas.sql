-- Tablas para CS1

CREATE TABLE Historicos_Ordenes (
    ID_Orden VARCHAR(10) PRIMARY KEY,
    ID_Equipo VARCHAR(10) NOT NULL, 
    Fecha DATE NOT NULL,            
    Tipo_Mantenimiento VARCHAR(20) NOT NULL CHECK (Tipo_Mantenimiento IN ('Correctivo', 'Preventivo')), 
    Tiempo_Reparacion_Horas INT NOT NULL CHECK (Tiempo_Reparacion_Horas > 0),  
    Costo_Mantenimiento NUMERIC(10, 2) NOT NULL CHECK (Costo_Mantenimiento >= 0),  
    Ubicacion VARCHAR(50) NOT NULL  
);

CREATE TABLE Resultados_Join (
    ID_Equipo VARCHAR(10) NOT NULL,             
    Fecha_Orden DATE NOT NULL,                  
    Tipo_Mantenimiento VARCHAR(20) NOT NULL,   
    Costo_Mantenimiento NUMERIC(10, 2) NOT NULL,
    Ubicacion VARCHAR(50) NOT NULL,            
    Fecha_Condicion DATE NOT NULL,             
    Horas_Operativas INT NOT NULL,             
    Temperatura_C NUMERIC(5, 2) NOT NULL,      
    Vibracion_mm_s NUMERIC(5, 2) NOT NULL,     
    Presion_Bar NUMERIC(5, 2) NOT NULL,        
    Horas_Acumuladas INT NOT NULL              
);