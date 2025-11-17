// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Interface
 * @dev Program 023
 */
contract Program023 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Interface");
    }
}
