// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Gasless Transaction
 * @dev Program 089
 */
contract Program089 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Gasless Transaction");
    }
}
