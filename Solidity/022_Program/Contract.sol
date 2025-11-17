// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Library
 * @dev Program 022
 */
contract Program022 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("Library");
    }
}
