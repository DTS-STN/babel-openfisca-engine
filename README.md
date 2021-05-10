# OpenFisca Canada Maternity Benefits System

This is an OpenFisca API that can be used for part of the EI calculation for maternity benefits, which is itself a special case of EI.

This project was based off of the OpenFisca country template: https://github.com/openfisca/country-template

All calculations use the "individual" as the entity.

## Parameters
The maternity benefit calculation has a number of fixed parameters that are used in calculating the eligible amount for any individual.

### max_weekly_amount
The maximum amount that an eligible applicant is entitled to per week. If their calculated amount exceeds this number, then they will receive this max_weekly_amount every week.

### number_of_weeks
This is the maximum number of weeks that an eligible applicant is able to receive benefits. 

### percentage
This is the percentage of an applicant's average income that they are entitled to receive on a weekly basis. For example, if an applicant's average income is 1000, and the percentage is 55%, then they would receive $550 per week. Not that the resulting number is also going to be bounded by the max_weekly_amount


## Variables

### maternity_benefits__entitlement_amount
The total amount that an eligible maternity applicant is eligible for.

### maternity_benefits__average_income
Average income of the applicant. This number is based on the applicant's average income for a certain number of weeks from the previous year. That number of weeks is based on the unemployment rate in their economic region. Note that this repo is currently not responsible for that part of the calculation. The value must already be known in order to calculate the entitlement amount.

### maternity_benefits__max_weekly_amount
This is an override for the max_weekly_amount parameter. This can be used if the user wants to simulate a rule change.

### maternity_benefits__percentage
This is an override for the percentage parameter. This can be used if the user wants to simulate a rule change.

### maternity_benefits__number_of_weeks
This is an override for the number_of_weeks parameter. This can be used if the user wants to simulate a rule change.

## Use case

This could potentially be used as a component by another application that handles the full maternity calculation. For example, that other application may ingest a record of employment or a list of weekly incomes. It would then calculate the average weekly income using that information (as well as other application information). The average income value could then be passed into this API to give the result of how much they are entitled to.

Since the main parameters for the maternity benefit calculation are overrideable by variables, this system can also be used to test potential rule changes. So if you want to see how changing the percentage or max_number_of_weeks may affect the amount that someone is eligible for, you can pass in variables to override those parameters. If you want to use the existing parameters, those variables can be left blank.

### Sample calculation:

```
POST /calculate
{
    "persons":  {
        "test_person": {
            "maternity_benefits__entitlement_amount": {"2020-08": null},
            "maternity_benefits__average_income": {"2020-08": 778},
            "maternity_benefits__max_weekly_amount": {"2020-08": 595},
            "maternity_benefits__number_of_weeks": {"2020-08": 15},
            "maternity_benefits__percentage": {"2020-08": 55}
        }
        
    }
}
```


## Development

### Running
The `build-run-dev` command in the Makefile can be run the API in a container, which can then be accessed from localhost:5000

### Testing
Once the API is running locally, tests can be run using the `test` command in the Makefile

