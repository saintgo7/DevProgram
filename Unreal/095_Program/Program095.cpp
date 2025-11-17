// Multicast RPC

#include "Program095.h"

AProgram095::AProgram095()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram095::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Multicast RPC ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating multicast rpc."));

    // Implement the program logic here...
}

void AProgram095::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
