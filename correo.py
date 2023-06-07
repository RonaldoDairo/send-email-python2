import smtplib
# Establecer conexion al servidor del correo SMTP
conexion = smtplib.SMTP(host='smtp.gmail.com', port=587)
conexion.ehlo()

# Encriptacion TlS
conexion.starttls()

# Iniciar sesion en el servidor SMTP
conexion.login(user='programaciondairo@gmail.com', password='tcocsjjbsamwaeqx')

# Enviar Correo
mensaje = 'Esto es una prueba'
conexion.sendmail(from_addr='programaciondairo@gmail.com', to_addrs='programaciondairo@gmail.com', msg=mensaje)


# Desconectar del servidor SMTP
conexion.quit()