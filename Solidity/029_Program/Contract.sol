// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Custom Errors
 * @dev Program 029
 */
contract Program029 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Custom Errors");
    }
}
