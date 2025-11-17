// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Struct
 * @dev Program 033
 */
contract Program033 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Struct");
    }
}
