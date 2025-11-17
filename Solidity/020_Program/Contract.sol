// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Reentrancy Guard
 * @dev Program 020
 */
contract Program020 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Reentrancy Guard");
    }
}
