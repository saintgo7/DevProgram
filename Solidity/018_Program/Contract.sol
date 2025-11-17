// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Role Based Access
 * @dev Program 018
 */
contract Program018 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Role Based Access");
    }
}
