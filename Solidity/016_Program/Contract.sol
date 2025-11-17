// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Ownable
 * @dev Program 016
 */
contract Program016 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Ownable");
    }
}
