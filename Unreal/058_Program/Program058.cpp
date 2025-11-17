// Load Level Async

#include "Program058.h"

AProgram058::AProgram058()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram058::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Load Level Async ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating load level async."));

    // Implement the program logic here...
}

void AProgram058::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
