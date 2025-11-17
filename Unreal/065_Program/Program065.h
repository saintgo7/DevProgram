// Physics Constraint
// Program 065

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program065.generated.h"

UCLASS()
class AProgram065 : public AActor
{
    GENERATED_BODY()

public:
    AProgram065();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
