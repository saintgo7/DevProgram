// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Error Handling
 * @dev Program 027
 */
contract Program027 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Error Handling");
    }
}
