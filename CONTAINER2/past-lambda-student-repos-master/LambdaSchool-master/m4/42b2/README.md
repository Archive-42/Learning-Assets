# Node DB 2 Module Challenge

In this challenge, you will write an API that can be used to manage _Cars_ stored in a Relational Database.

## Project Set Up

Follow these steps for starting your project.

- [x] Fork this repository into your account and **clone your version**.
- [x] Add your _Team Lead_ as collaborator on your repository.
- [x] Create a new branch: git checkout -b `<firstName-lastName>`.
- [x] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly.
- [x] Push commits: git push origin `<firstName-lastName>`.

Follow these steps for completing your project.

- [x] Submit a Pull-Request to merge `<firstName-lastName>` Branch into master (student's Repository). **Please don't merge your own pull request**
- [x] Add your _Team Lead_ as a reviewer on the pull-request
- [x] Your _Team Lead_ will count the project as complete by merging the branch back into master.

## Minimum Viable Product

- [x] Using `knex migrations`, design and write a schema for the `cars` table using the specifications below.
- [x] Configure `knex` to connect to a `/data/car-dealer.db3` database using the `sqlite3` npm module.
- [x] Write endpoints to support `CREATE` and `READ` operations on the `cars` resource.
- [x] Use a rest client like _Insomnia_ or _Postman_ to test your API.

## Specifications

The client for this API is a car dealer who has provided the following specs:

- [x] The critical information for each car is the VIN, make, model, and mileage.
- [x] They also track transmission type and status of the title (clean, salvage, etc.), but this information is not always immediately known.

## Stretch Problems

- [x] Add seed data to the database using `knex seeds`
- [x] Add `UPDATE` and `DELETE` operations to your API.
- [ ] Write a schema file for a `sales` table. This table should track information on the sale of each car. You may wish to research `foreign keys` in order to link each sale to the entry in `cars` which sold.
