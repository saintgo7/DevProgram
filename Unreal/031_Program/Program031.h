// Animation Blueprint
// Program 031

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program031.generated.h"

UCLASS()
class AProgram031 : public AActor
{
    GENERATED_BODY()

public:
    AProgram031();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
