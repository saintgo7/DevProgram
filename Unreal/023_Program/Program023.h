// Blueprint Pure
// Program 023

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program023.generated.h"

UCLASS()
class AProgram023 : public AActor
{
    GENERATED_BODY()

public:
    AProgram023();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
