// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SafeMath
 * @dev Program 021
 */
contract Program021 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("SafeMath");
    }
}
