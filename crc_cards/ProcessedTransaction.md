# ProcessedTransaction

A complete transaction which has sucessfully been processed

## Details

<!-- List out the key attributes of the class here -->
* List\<Item>
* Payment
* Time

## Responsibilities

<!-- List out the responsibilites here -->
* Knows
  * The items the transaction purchased
  * The time of the transaction
  * The payment used for the transaction
* Does
  * Generates the correct represenation for storage in the database

## Connections

<!-- List out the classes this class will interact with -->
* UnprocessedTransaction
* Database
