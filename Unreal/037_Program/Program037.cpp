// Behavior Tree

#include "Program037.h"

AProgram037::AProgram037()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram037::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Behavior Tree ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating behavior tree."));

    // Implement the program logic here...
}

void AProgram037::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
