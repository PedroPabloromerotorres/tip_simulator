from formula.logic import calcular_propina, calcular_total_con_propina, dividir_total
import os
def desing():
    option = 1 
    while option:
        print(f"""
        =============================================
            Dividir Cuenta entre Varias Personas
        =============================================""")
        total = float(input(     "Ingrese el monto total de la cuenta: $"))
        porcentaje = int(input("Ingrese el porcentaje de propina (por ejemplo: 10, 15, 20): "))
        persona = int(input("Ingrese el número de personas: "))
        propina = calcular_propina(total, porcentaje)
        totalmaspropina = calcular_total_con_propina (total, propina)
        print(f"""
        =============================================
        La propina calculada es: ${propina}
        El total a pagar es: ${totalmaspropina}
        Monto por persona: ${dividir_total(totalmaspropina, persona)}
        =============================================""")
        option = int(input("¿Deseas calcular nuevamente? (1-S/0-N): "))
        os.system('clear')