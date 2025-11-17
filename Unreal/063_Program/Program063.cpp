// Add Force

#include "Program063.h"

AProgram063::AProgram063()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram063::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Add Force ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating add force."));

    // Implement the program logic here...
}

void AProgram063::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
