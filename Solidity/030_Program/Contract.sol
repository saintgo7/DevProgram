// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Try Catch
 * @dev Program 030
 */
contract Program030 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Try Catch");
    }
}
