# UnprocessedTransaction

A pending transaction contstructed by an employee which needs to have payment
and items validated

## Details

<!-- List out the key attributes of the class here -->
* List\<Item>
* Time
* Payment

## Responsibilities

<!-- List out the responsibilites here -->
* Knows
  * The items the transaction purchased
  * The time of the transaction
  * The payment used for the transaction
* Does
  * Communicates with verification processes to generate a `ProcessedTransaction`
  * Offers an interface to be created from user input

## Connections

<!-- List out the classes this class will interact with -->
* ProcessedTransaction
* Database
* *RPC Communications*
