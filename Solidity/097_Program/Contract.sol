// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Overflow Check
 * @dev Program 097
 */
contract Program097 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Overflow Check");
    }
}
