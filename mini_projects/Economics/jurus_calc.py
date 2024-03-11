

pretend_value: float = 800
taxes_incoming: float = 4.49
taxes_on_payment: float = 8.5
months: int = 5


final_taxes: float= (taxes_incoming/100)*pretend_value + (taxes_on_payment/100)*pretend_value
final_value: float = pretend_value - final_taxes

print(f'Total taxes: {final_taxes:.2f}\n'
      f'Final value: {final_value:.2f}')