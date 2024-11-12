from formula.logic import calcular_propina, calcular_total_con_propina 
import os 
def desing():
    option = 1
    while option 
        print(f"""
        =============================================
                 Cálculo de Propina
        =============================================""")
        total = float(input("    Ingrese el monto total de la cuenta: $"))
        porcentaje = int(input( "    Ingrese el porcentaje de propina (por ejemplo: 10, 15, 20): "))
        propina = calcular_propina(total, porcentaje )
        print(f"""
        =============================================
        La propina calculada es: ${propina}
        El total a pagar es: ${calcular_total_con_propina(total, propina)}
        =============================================
        """)
        input("¿Deseas calcular nuevamente? (S/N)")
        os.system("clear")
    else:
        break
    