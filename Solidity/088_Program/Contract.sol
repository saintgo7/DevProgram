// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Meta Transaction
 * @dev Program 088
 */
contract Program088 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Meta Transaction");
    }
}
