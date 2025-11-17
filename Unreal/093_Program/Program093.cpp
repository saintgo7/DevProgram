// Server RPC

#include "Program093.h"

AProgram093::AProgram093()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram093::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Server RPC ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating server rpc."));

    // Implement the program logic here...
}

void AProgram093::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
