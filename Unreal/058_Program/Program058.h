// Load Level Async
// Program 058

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program058.generated.h"

UCLASS()
class AProgram058 : public AActor
{
    GENERATED_BODY()

public:
    AProgram058();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
