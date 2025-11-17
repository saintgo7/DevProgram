// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Function Visibility
 * @dev Program 073
 */
contract Program073 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Function Visibility");
    }
}
