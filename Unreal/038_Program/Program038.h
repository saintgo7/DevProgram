// Blackboard
// Program 038

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program038.generated.h"

UCLASS()
class AProgram038 : public AActor
{
    GENERATED_BODY()

public:
    AProgram038();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
