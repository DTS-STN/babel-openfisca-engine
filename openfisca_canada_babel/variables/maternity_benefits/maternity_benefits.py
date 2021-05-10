# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
from openfisca_core.periods import ETERNITY, MONTH

# Import the entities specifically defined for this tax and benefit system
from openfisca_canada_babel.entities import Person

class maternity_benefits__entitlement_amount(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    default_value = 0

    def formula(persons, period, parameters):
        potential_value = persons('maternity_benefits__average_income', period) * persons('maternity_benefits__percentage', period) / 100
        weekly_value = min(potential_value, persons('maternity_benefits__max_weekly_amount', period))
        return weekly_value * persons('maternity_benefits__number_of_weeks', period)

class maternity_benefits__average_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    default_value = 0

class maternity_benefits__max_weekly_amount(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH

    def formula(person, period, parameters):
        return parameters(period).maternity_benefits.max_weekly_amount

## This is for all of EI. Maybe use that parameter under the hood
class maternity_benefits__percentage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH

    def formula(person, period, parameters):
        return parameters(period).maternity_benefits.percentage

class maternity_benefits__number_of_weeks(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH

    def formula(person, period, parameters):
        return parameters(period).maternity_benefits.number_of_weeks