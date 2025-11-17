// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Proxy Pattern
 * @dev Program 062
 */
contract Program062 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Proxy Pattern");
    }
}
