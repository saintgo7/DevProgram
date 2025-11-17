// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Enum
 * @dev Program 034
 */
contract Program034 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Enum");
    }
}
