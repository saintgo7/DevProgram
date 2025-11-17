// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Access Check
 * @dev Program 098
 */
contract Program098 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Access Check");
    }
}
